"use strict"

var main = function(i) {
    for (var x of i) {
        console.log(x)
    }
}
let y = [1,2,3,4,5]

function func(...params) {
    var x = params
    console.log(x)
}

var f = new Function('i', 'console.log(i)')

//var t = new func(1)

//var a = new main([6,7,8,9])
//a([1,2,3,4])
//a.new_property1 = 'ab'

//console.log(a.new_property1)
//console.log(main.new_property1)

var a = 0
console.log(a === false)
/*
f('b')
main(y)
func('asdf', 'd', '123')
*/