"#convert_protocal" 
问题引出
假设有这样一种需求，JSON类型的协议组A中的数据需要经过某种转换变成另外一种JSON类型的协议族B，普通的做法是从协议A中A1开始，逐个取出值， 然后再"静态"的存储到协议族B中的B1对应的字段中，这样的做法有两种缺点：
1.转换协议的代码会随着协议的变动而变动，程序与数据耦合，开发人员需要不断地维护和更新软件版本
2.协议族中具体协议数量决定了转换代码的数量，协议族中协议越多，转换代码就越多，重复工作量大

解决方案
为了解决协议转换的问题，同时避免冗余代码，可以使用算法+转换规则来解决，即制定某种规则P，开发动态生成协议的方法F，协议指代类型T，用形式化的方法表达如下：
F(P, T, A) -> B
这个五元数的意义是：某种具体协议T， 在使用规则P的前提下，根据方法F把具体JSON类型的协议对象A转换为协议对象B

使用方法：
现有某种类型的协议A的具体对象,代表某种工厂的具体产品：
val = {
	"ID"："1",
	"Type": "scr_type",
	"Factory":{
		"ID"："001-002",
		"Address": "Orleans-oldMill-1-101",
		"Manager":{
			"ID":"002",
			"Name":"Joan Mary"
		},
	"Name":"deak lamp",
	"Weight":"200g",
	"Material":{
		"M1":"Fe",
		"M2":"wire",
		"M3":"Cu"
		}
	},
	"DateOfManufacture":"2019-08-01 8:15 AM"
}

需要转换成满足协议B的对象
to = {
	"ID"："1",
	"Property":{
		"Type": "scr_type",
		"Weight":"200g",
		"Company":{
			"ID"："001-002",
			"Address": "Orleans-oldMill-1-101",
			"Manager":{
				"ID":"002",
				"Name":"Joan Mary"
			},
		"Name":"deak lamp",
		"M1":"Fe",
		"M2":"wire",
		"M3":"Cu"
		},
	"DateOfManufacture":"2019-08-01 8:15 AM"
	}
}

制定转换的规则，用：分隔AB两种协议，A协议在：右侧，B协议在：左侧，各个属性之间用，分隔 ，属性内层级用|分隔，如果属性从根层次开始就不需要|，直接写属性即可，上述转换的规则是：
policy=
"ID,Property|Type,Property|Weight,Property|Company|ID,Property|Company|Address,Property|Company|Manager|ID,Property|Company|Manager|Name,Property|Name,Property|M1,Property|M2,Property|M3,DateOfManufacture:
ID,Type,Factory|Weight,Factory|ID,Factory|Address,Factory|Manager|ID,Factory|Manager|Name,Factory|Name,Factory|Material|M1,Factory|Material|M2,Factory|Material|M3,DateOfManufacture"
应该如此使用函数
convert_protocol(policy, "convert_Example", val)
即可得到上述的to对象。
