from lib.objects import *
import lib.config as config


class DBA:
    __table_name__ = config.table_name
    __conn__ = config.conn
    __cursor__ = __conn__.cursor()
    objects = Objects()

    def __init__(self,**kwargs):
        self.__conn__ = self.__conn__
        self.__cursor__ = self.__cursor__
        self.__table_name__ = self.__table_name__
        self.create_all()
        self.__dict__.update(kwargs)


    def insert_msg(self, id, msg, address, reply):
        try:
            self.__cursor__.execute("INSERT OR IGNORE INTO Messages(id, msg, address,reply) VALUES(?,?,?,?)",
                      (id, msg, address, reply))
        except:
            return None
        else:
            self.__conn__.commit()
            # conn.close()
            return True

    def query_msg(self, **kwargs):
        try:
            self.__cursor__.execute("SELECT * FROM Messages WHERE id={id}".format(id=id))
        except:
            return None
        else:
            return self.__cursor__.fetchall()

    def create_all(self):
        values = []
        names = self.get_var_names()
        des = []
        for i in self.get_var_values():
            des.append(vars(i))
        #print(des)
        #print(self.get_var_values())
        for i,desc in zip(self.get_var_values(),des):
            if isinstance(i, models.CharField):
                values.append('TEXT')
            if isinstance(i, models.IntegerField):
                if desc['PRIMARY_KEY']==True:
                    values.append("INTEGER PRIMARY KEY,")
                else:
                    values.append("INTEGER,")
            if isinstance(i, models.FloatField):
                values.append("REAL")
        #print(des)
        config.columns = names
        sql = "CREATE TABLE IF NOT EXISTs {}".format(self.__table_name__)

        for index,(name,value,d) in (enumerate(zip(names,values,des))):
            #print(values[index])
            if index == 0:
                sql += "({} {}".format(name, value)
                if des[index].values():
                    for i in des[index].values():
                        if "INTEGER" not in values[index]:
                            sql += "({}),".format(i)
                else:
                    sql += ","
            elif index > 0 and index != len(values)-1:
                sql += "{} {}".format(name, value)
                if des[index].values():
                    for i in des[index].values():
                        if "INTEGER" not in values[index]:
                            sql += "({}),".format(i)
                else:
                    sql += ","
            else:
                sql += "{} {}".format(name, value)
                if des[index].values():
                    for i in des[index].values():
                        if "INTEGER" not in values[index]:
                            sql += "({}))".format(i)
                else:
                    sql += ")"
        # sql.replace(".",")")
        #print(sql)
        try:
            self.__cursor__ .execute(sql)
        except Exception as e:
            #print(e)
            return False
        else:
            #print(self.__tablename__ ," created")
            return True


    def all_vars(self):
        var = {}
        for name, value in self.__class__.__dict__.items():
            if not name.startswith("__"):
                var[name]=value
        return var
        #all = print(self.__class__.__dict__.items())#vars(DBA)
        #return all

    def get_var_names(self):
        var = []
        for each in self.__class__.__dict__:
            if not each.startswith("__"):
               var.append(each)
        return var

    def get_var_values(self):
        var = []
        for name,value in self.__class__.__dict__.items():
            if not name.startswith("__"):
                var.append(value)
        return var

    def save(self):
        all = {}
        sql = "INSERT OR IGNORE INTO {}".format(self.__table_name__)
        mydict = vars(self)
        #print(mydict)
        for index,(key,value) in enumerate((mydict.items()),0):
            if not key.startswith("__") and not key =="objects":
                all[key]=value
        #print(all)
        for index, (key, value) in enumerate((all.items()), 0):
            if index < 1:
                sql += "({}".format(key)
            elif index > 0 and index != len(all.values())-1:
                sql += " ,{},".format(key)
            else:
                sql += " {}".format(key)
        sql +=") VALUES"

        for index, (key, value) in enumerate((all.items()), 0):
            if index < 1:
                if type(value) is int:
                    sql+="({}".format(value)
                else:
                    sql += "('{}'".format(value)
            elif index > 0 and index != len(all.values())-1:
                if type(value) is int:
                    sql += ",{},".format(value)
                else:
                    sql += ",'{}',".format(value)
            else:
                if type(value) is int:
                    sql += "{}".format(value)
                else:
                    sql += "'{}'".format(value)
            sql+=")"
        #print(sql)
        try:
            self.__cursor__ .execute(sql)
        except Exception as e:
            #print(e)
            return False
        else:
            #print(" saved")
            self.__conn__.commit()
            object = self
            return object

