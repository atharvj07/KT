var n=Number(readline());
var res=0;
var c=["ABSINTH", "BEER", "BRANDY", "CHAMPAGNE", "GIN", "RUM", 'SAKE', 
'TEQUILA', 'VODKA', 'WHISKEY', "WINE"];
for (var i=0; i<n; i++) {
    var x=readline();
    if (c.includes(x)) {
        res+=1;
    }
    else if (/^\d+$/.test(x)&&Number(x)<18) {
        res+=1;
    }
}
print(res);