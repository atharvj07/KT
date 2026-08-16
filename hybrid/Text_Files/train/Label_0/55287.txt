var useless = readline();
var drinks = readline().split(" ");
var result = drinks.reduce((cur,acc) => Number(acc)+Number(cur) ,0);
var answer = result/drinks.length;
print(answer)