from django.core.mail import send_mail

from .models import OrderItem, Order



def send_mail_customer(order_id):
    order = Order.objects.get(id=order_id)
    products_in_order=OrderItem.objects.filter(order__id=order_id)
    letter_list=''
    for product in OrderItem.objects.filter(order__id=30):
        letter_list+=("{}  количество: {} цена: {}\n".format(product.product, product.quantity, product.price))
    subject = 'Заказ № {}'.format(order.id)
    message = """Уважаемый(ая) {},\n\nВаш заказ успешно размещён.\nID Вашего заказа: {}.\n
    Подробности заказа:\n{}\nМенеджер свяжется с Вами в ближайшее время для уточнения деталей.
    """.format(order.first_name, order.id, letter_list)
    mail_sent = send_mail(subject, message, 'site-childstore@gmail.com', [order.email])
    return mail_sent

def send_mail_admin(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Новый заказ № {}'.format(order.id)
    message = """На сайте размещён новый заказ, ID заказа: {}.""".format(order.id)
    mail_sent = send_mail(subject, message, 'site-childstore@gmail.com', ['site-childstore@gmail.com'])
    return mail_sent
