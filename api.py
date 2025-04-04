import db
# Implementing API for db and bot
# REPORTING
def get_money(acc_hex):
    if is_there(acc_hex) == True:
        sql = """SELECT Price 
        FROM acc_price 
        WHERE Account_Hex = %s"""
        val = [acc_hex]
        db.cur.execute(sql, val)
        res = db.cur.fetchone()
        return res
    else:
        return 404

def is_there(acc_hex):
    sql = """SELECT Account_Hex 
    FROM acc_price"""
    db.cur.execute(sql)
    for record in db.cur:
        if acc_hex in record:
            return True
    return False

def get_all():
    sql = """SELECT Account_Hex, Price 
    FROM acc_price"""
    db.cur.execute(sql)
    return db.cur.fetchall()

# SETTING
def set_money(acc_hex, money):
    if is_there(acc_hex):
        sql = """UPDATE acc_price 
        SET Price = Price + %s
        WHERE Account_Hex = %s"""
        val = [money, acc_hex]
    else:
        sql = """INSERT INTO acc_price (Account_Hex, Price, status)
        VALUES (%s,%s,0)"""
        val = [acc_hex, money]
    db.cur.execute(sql, val)
    db.db.commit()
    return 200


def reset_money(acc_hex):
    if is_there(acc_hex): 
        sql = """UPDATE acc_price 
        SET Price = 0
        WHERE Account_Hex = %s"""
        val = [acc_hex]
        res = db.cur.execute(sql, val)
        db.db.commit()
        return 200
    else:
        return 404
