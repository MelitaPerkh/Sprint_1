types = {
        1: 'Блокирующий',
        2: 'Критический',
        3: 'Значительный',
        4: 'Незначительный',
        5: 'Тривиальный'
    }

tickets = {
        1: ['API_45', 'API_76', 'E2E_4'],
        2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
        3: ['E2E_45', 'API_45', 'E2E_2'],
        4: ['E2E_9', 'API_76'],
        5: ['E2E_2', 'API_61']
    }

def delDouble(ticketsArg):
    ticketsCopy={}
    unicTicket = []
    for key, ticket in ticketsArg.items():
        ticketsCopy[key]=[]
        for i in ticket:
            if i not in unicTicket:
                 ticketsCopy[key].append(i)
                 unicTicket.append(i)
            
    return ticketsCopy
   

def ticketsByType(types, tickets):
    tickets_by_type = {}
    for key,value in types.items():
        if key in tickets.keys():
            tickets_by_type[value] = tickets[key]
    return tickets_by_type


tickets = delDouble(tickets)
result = ticketsByType(types, tickets)
