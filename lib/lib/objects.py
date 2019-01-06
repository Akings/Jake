import lib.config as config


class Objects:
    __tablename__ = config.table_name
    __conn__ = config.conn
    __cursor__ = __conn__.cursor()

    def __init__(self,*args):
        pass
        #if args:
        #    self.__tablename__= args[0]
        #    self.__conn__ = args[1]
        #    self.__cursor__ = args[2]

    class Object:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

        class Meta:
            verbose_name = "Message"

        def __str__(self):
            return '%s' % (self.id)

    def all(self):
        results = []
        pairs = []
        pairer = []
        sql = "SELECT * FROM {}".format(self.__tablename__)
        print(sql)
        try:
            result = self.__cursor__.execute(sql)
        except Exception as e:
            return e
        else:
            result = result.fetchall()
            if result is None:
                return None
            #print(result)
            #print(config.columns)
            for each in result:
                obj = self.Object()
                count = 0
                for i in each:
                    obj.__setattr__(config.columns[count],i)
                    pairs.append((config.columns[count],i))
                    count+=1
                results.append(obj)
                del obj
            #print(pairs)
            return results

    def get(self,**kwargs):
        results = []
        pairs= []
        if kwargs:
            sql = "SELECT * FROM {}".format(self.__tablename__)
            for index, (key, value) in enumerate(kwargs.items(), 1):
                if index < 2:
                    sql += " WHERE {} = '{}'".format(key, value)
                else:
                    sql += " AND {} = '{}'".format(key, value)
        else:
            sql = "SELECT * FROM {}".format(self.__tablename__)
        try:
            result = self.__cursor__.execute(sql)
        except Exception as e:
            print(e)
            return None
        else:
            if result is None:
                return None
            for each in result:
                obj = self.Object()
                count = 0
                for i in each:
                    obj.__setattr__(config.columns[count],i)
                    pairs.append((config.columns[count],i))
                    count+=1
                results.append(obj)
                del obj
            #print(pairs)
            return results[0]


class models:
    class CharField:
        def __init__(self, max_length,**option):
            self.max_length = max_length

    class IntegerField:
        def __init__(self, **options):
            self.__dict__.update(options)

    class FloatField:
        def __init__(self):
            pass
