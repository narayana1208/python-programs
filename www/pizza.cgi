#!/usr/bin/python

'''Script to process pizza orders.  The output page depends on whether
the client name is a special OWNER string.  If so, past orders are read and
displayed from an order file.  Otherwise a normal order is taken and recorded.
This version keeps only one copy of the data on sizes, toppings and costs,
and actively embeds the data in the form.
The only changes from pizza1.cgi are in the function processCustomer.
'''

import cgi   

OWNER = 'owner777'  # owner must know this string to use as the name!
ORDER_FILE = 'pizzaOrders.txt'

def main():
    form = cgi.FieldStorage()      
    
    client = form.getfirst('client', '')
    if client == OWNER:  # special case for identified owner
        print processOwner()
    else:
        size = form.getfirst('size', '') 
        toppings = form.getlist('topping') # note getting *list*
        pastState = form.getfirst('pastState', '')
        print processCustomer(client, size, toppings, pastState)
    
def processCustomer(client, size, toppings, state):  
    '''Process customer input parameters and return the final page as a string.
    The same basic form is used for the initial page as well as later pages,
    since the customer is encouraged to order multiple pizzas.
    The ONLY location of the pizza options and costs is here.
    This data is placed in the order form.'''

    # The main changes from pizza1.cgi are at the beginning of this function,
    #   creating the strings sizeOptions and toppingOptions.
    
    # basic pizza data
    costData = dict() # values for sizes: (baseCost, extra cost per topping)
    costData['small'] = (5.50, .50)
    costData['medium'] = (7.85, .75)
    costData['large'] = (10.50, 1.00)
    sizes = ['small', 'medium', 'large'] # dictionary key order not useful

    allToppings = ['pepperoni', 'sausage', 'onions', 'mushrooms','extra cheese']
    # end of basic pizza data
    
    # derived from standard radio button line in pizzaOrderTemplate1.html source
    sizeTemplate = '''<input name="size" value="%s" type="radio">
                      %s: &nbsp;$%.2f plus $%.2f per topping<br>'''
    sizeOptions = ''
    for option in sizes:
        # can concatenate tuples like other sequences!
        substitutions = (option, option.capitalize()) + costData[option]
        sizeOptions +=  sizeTemplate % substitutions

    # derived from standard check box line in pizzaOrderTemplate1.html source
    toppingTemplate = '<input name="topping" value="%s" type="checkbox"> %s<br>'
    toppingOptions = ''
    for option in allToppings:
        toppingOptions += toppingTemplate % (option, option.capitalize())
        
    if not state == 'order':  # initial display of order form
        msg = ''
        invitation = 'Please fill out and submit your order.'
        state = 'order'
    elif not client or not size:  # must have a name and size entered
        msg = '<p><b>You must enter your name and a pizza size with an order!</b></p>'
        invitation = 'Please fill out and submit your order.'
        state = 'order'
    else:  # with a name and size, assume a real order
        if toppings:
            toppingString = ', '.join(toppings)
        else:
            toppingString = 'None'

        # Aside from including sizeOptions and toppingOptions in the output,
        #   the rest of the function is the same as in pizza1.cgi
        (baseCost, toppingCost) = costData[size]
        cost = baseCost + toppingCost * len(toppings)
        msg = '''<p>%s:  Your ordered a %s pizza; toppings: %s.<br>
        The cost is $%.2f.  Please pick it up in 30 minutes.<br>
        Thank you for your order!</p>
        '''  % (client, size, toppingString, cost)
        line = '%s; $%.2f; %s; %s\n' % (client, cost, size, toppings)
        append(ORDER_FILE, line)
        invitation = 'If you want another pizza, please order again.'
        state = 'order'
    return makePage('pizzaOrderTemplate.html',
                  (msg, invitation, client, sizeOptions, toppingOptions, state))

def processOwner():
    '''Display all orders from the order file.'''
    return makePage('pizzaReportTemplate.html',fileLinesToHTMLLines(ORDER_FILE))
    
# standard functions and code from here on
def append(fileName, s):
    """Append string s to file with name fileName.
    This fails if there are multiple people trying simultaneously.
    """
    fout = open(fileName,'a') # 'a' means append to the end of the file
    fout.write(s)
    fout.close()

def safePlainText(s):
    '''Return string s with reserved html markup characters replaced
    and newlines replaced by <br>.'''
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('\n', '<br>')

def fileLinesToHTMLLines(fileName):
    """Allow lines of the file with name fileName to be embedded in html.
    This fails if there are multiple people trying.
    """
    
    lines = fileToStr(fileName).splitlines()
    safeLines = list()
    for line in lines:
        safeLines.append(safePlainText(line))
    return "<br>\n".join(safeLines)


def fileToStr(fileName): 
    """Return a string containing the contents of the named file."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close() 
    return contents

def makePage(templateFileName, substitutions): 
    """Returns a string with substitutions into a format string taken
    from the named file.  The single parameter substitutions must be in
    a format usable in the format operation: a single data item, a
    dictionary, or an explicit tuple."""

    pageTemplate = fileToStr(templateFileName)
    return  pageTemplate % substitutions

try:   
    print "Content-type: text/html\n\n"   
    main() 
except:
    cgi.print_exception()               

