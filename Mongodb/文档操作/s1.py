#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/24 10:11

"""
插入
1.
db.集合名.insert(document)
db.student.insert([{name:'张三',age:20},{name:"李四",age:32}])

2.
使用save()
db.集合名.save(文档)
如果不指定_id字段，save()类似Insert()
如果指定，则会更新_id字段
db.student.save([{name:'donghao',age:20},{name:"tanyajuan",age:20}])
db.student.save({_id:ObjectId("5cbfc71860f9d864da892f17"),name:"hahahah",age:100}) "nUpserted"
"""


"""
文档更新
1.  update() 更新已存在的文档
    db.集合名.date(
        query,
        update,
            {
                upset:<boolean>,
                multi: <boolean>,
                writeConcern: <document>
            }
    )
    参数：
    query:  查询条件
    update: 更新操作符 ($set,$inc)等
    $set：直接更新   $inc：原基础上累加后更新
    
    upset： 可选：如果不存在update数据，是否插入新数据（当新数据插入）
        true :插入  false :不插入   默认false
      
     multi:  默认是false.只更新第一条记录，
     
     writeConcern：  抛出异常级别
     
db.student.update({name:"hahahah"},{$set:{age:111}})      
db.student.update({name:"donghao"},{$set:{age:666}},{multi:true})    #全改


2.  方法通过传入的替换已有文档(伪更新)
db.集合名.save(
    document,
          {
                writeConcern: <document>
            }
    )
    
3. 删除

执行remove()函数前，先执行find()来判断是否存在    
db.集合名.执行remove(
    query,
    {
        justOne: <boolean>,
        writeConcern: <document>
    }
)   

db.student.remove({name:"张三"})


4. 查找


    db.集合名.find(
        query,
        {
            <key>:1,
            <key>:2    
        }
    )
    db.student.find({},{name:1}) #只看年龄
    
    
    pretty() 方法 以格式化的方式来显示文档
    db.student.find({},{name:1}).pretty()

5. 查询条件操作符
***************db.集合名.find({<key>,{比较:<value>}})
a    大于  $gt   db.student.find({age:{$gt:20}})
b    大于等于  $gte db.student.find({age:{$gte:20}})
c    小于  $lt   db.student.find({age:{$lt:20}})
d    小于等于 $lte   db.student.find({age:{$lte:20}})

db.student.find({age:{$lte:20,$gte:2}})
e    等于  : 
f    使用_id 查询  db.student.find({_id:ObjectId("5cbfd02760f9d864da892f21")})
g    count   db.student.find().count()
h    包含  db.student.find({name:/dong*})
i    开头  db.student.find({name:/^dong/})
j     and  db.student.find(gender:xx,age:{$gt:20})
k     or 
     db.集合.find({
            $or:[
            
            条件1，
            条件2
            ...
            ]
        })
db.student.find({$or:[{name:/dong/},{age:32}]})

and or 联合使用

db.xx.find({条件1，条件2,$or:[{条件1，条件2}]})



limit,skip

limit:
 db.student.find().limit(2)
 db.student.find().skip(2) 跳过


 db.student.find().skip(2).limit(2)
 
 
 排序
 db.xxx.find().sort({<key>:1|-1})
 db.student.find().sort({age:1})
  1:  升序
 -1：降序
"""









