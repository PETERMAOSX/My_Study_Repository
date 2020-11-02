function Person(name,number,sex){
    this.name = name;
    this.number = number;
    this.sex = sex;
}
var Shaoxiong = new Person("Maoshaoxiong",1815000094,"Boy");
console.log("Name: "+Shaoxiong.name+"\n"
+"Number: "+Shaoxiong.number+"\n"
+"Sex: "+Shaoxiong.sex
);