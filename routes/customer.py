from flask import Blueprint,render_template,request
from database.client import Clients

customer_route = Blueprint('customer',__name__)

@customer_route.route('/')
def list_customers():
    return render_template('list_customers.html',clients = Clients)

@customer_route.route('/',methods=['POST'])
def insert_customer():
    data = request.json

    new_client = {
        'id':len(Clients)+1,
        'name':data['name'],
        'email':data['email'],
    }

    Clients.append(new_client)
    return render_template('item_customer.html',client=new_client)

@customer_route.route('/new')
def form_customer():
    return render_template('form_customer.html')


@customer_route.route('/<int:customer_id>')
def datail_customer(customer_id):
    pass


@customer_route.route('/<int:customer_id>/edit')
def edit_customer(customer_id):
    client = None
    for c in Clients:
        if c['id'] == customer_id:
            client = c
    return render_template('form_customer.html',client=client)


@customer_route.route('/<int:customer_id>/update',methods=['PUT'])
def update_customer(customer_id):
    pass


@customer_route.route('/<int:customer_id>/delete',methods=['DELETE'])
def delete_customer(customer_id):
    global Clients
    Clients = [c for c in Clients if c['id'] != customer_id]
    return {'Deleted!':'ok'}
