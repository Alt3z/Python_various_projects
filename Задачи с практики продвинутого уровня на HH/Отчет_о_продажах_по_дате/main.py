class Item:
    def __init__(self, date, product, quantity):
        self.date = date
        self.product = product
        self.quantity = int(quantity)


def generate_product_report(data):
    product = {}
    for record in data.split(";"):
        prod = Item(*record.split(":"))

        if prod.product not in product:
            product[prod.product] = [prod.date, prod.quantity]

        else:
            count = 0
            flag = True
            flag_2 = True
            for item in product[prod.product]:
                if flag == True:
                    flag = False
                    if item == prod.date:
                        product[prod.product][count+1] += prod.quantity
                        flag_2 = False
                        break
                else :
                    flag = True
                count += 1
            if flag_2 == True:
                product[prod.product] += [prod.date, prod.quantity]

    output_mas = []
    for prod in product.keys():
        s = f"{prod}:"
        for record in product[prod]:
            if isinstance(record, str):
                s += f"\n- {record}:"
            else:
                s += f"{record}"
        output_mas.append(s)

    return output_mas


input_data =  input()

product_report_generator = generate_product_report(input_data)
for report in product_report_generator:
    print(report)