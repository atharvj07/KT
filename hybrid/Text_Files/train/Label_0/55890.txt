var ip = readline().split(' ').map(Number);
var n = ip[0], open = ip[1]/2, close = ip[1]/2, res = '';
readline().split('').forEach(x=>{
   if (x === '(' && open !== 0){
       open--;
       res += x;
   }  else if (x === ')' && close !== 0){
       close--;
       res += x;
   }
});
print(res)