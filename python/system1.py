# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 10:21:58 2020

@author: zhao
"""
import pymysql
import DBUtils
import random
import sys
import time
class System1:
    def createConnection(self,signal=True):
        if signal==True:
            POOL = DBUtils.PooledDB(
                creator=pymysql,  # 使用链接数据库的模块
                maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
                mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
                maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
                maxshared=3,  # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
                blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
                maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
                setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
                ping=0,
                # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
                host='49.232.6.143',
                port=3306,
                user='root',
                password='sdfe@#$QW',
                database='sm_enterprise',
                charset='utf8'
                )
        return self.POOL.createConnection()
    def __init__(self):
        # 数据库构造函数，从连接池中取出连接，并生成操作游标
        self.conn = self.createConnection(self,True).connection()
        self.cursor = self.conn.cursor()
    def judgeData(self,userId,pageId=0):
    # 检测当前正在运行连接数的是否小于最大链接数，如果不小于则：等待或报raise TooManyConnections异常
     # 否则
    # 则优先去初始化时创建的链接中获取链接 SteadyDBConnection。
    # 然后将SteadyDBConnection对象封装到PooledDedicatedDBConnection中并返回。
    # 如果最开始创建的链接没有链接，则去创建一个SteadyDBConnection对象，再封装到PooledDedicatedDBConnection中并返回。
    # 一旦关闭链接后，连接就返回到连接池让后续线程继续使用。
        self.cursor.execute('select  from tb1 where id is userId')#判断公司的信息是否完善
        judgeResult = self.cursor.fecthone()
        if judgeResult==1:
            print('enough imfo!')
            self.cursor.execute('select * from table order by time desc')
            self.col=self.cursor.fetchall()
            self.col=self.col.extend(self.final)
            if (pageId*10-len(self.final)>=10):
                return self.col[pageId*10:pageId*10+9]
            else:
                return self.col[pageId*10:]
            
        else:
            print('Incomplete information')
            if (pageId*10-len(self.final)>=10):
                return self.final[pageId*10:pageId*10+9]
            else:
                return self.final[pageId*10:]
            
    def recommend(self,userId):
        self.cursor.execute('select businessScope from table where id is %d',userId)
        outcome=self.cursor.fetchone()
        new=[]
        final=[]
        for i in outcome:
            self.cursor.execute('select id from table where label like "@i" ' )
            new.extend(self.cursor.fetchall())
        new=set(new)
        self.cursor.execute('select * from table where id in {} order by time desc'.format(*new))
        self.final=self.cursor.fetchall()
        return self.final


        
                    
            
        
        

        
        
        
        
        
        
        
        
    
    