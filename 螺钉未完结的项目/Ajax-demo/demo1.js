var jstu='{"name":"张奔","age":18}';
console.log(jstu);
var obj = JSON.parse(jstu);
console.log(obj.name);
// JSON是一种文本格式,可以把后台返回的数据转换成对象,取到相对应的数据
console.log(typeof jstu);
console.log(typeof obj);
var obj2 = JSON.stringify(jstu);
console.log(typeof obj2)