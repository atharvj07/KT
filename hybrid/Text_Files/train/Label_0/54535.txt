import java.util.*;
 
public class Main {
    static Scanner sc = new Scanner(System.in);
    static int keisan(int a,int b,int c,int d){
        char cms[] = {'+','-','*'};
        for(int i = 0;i < 3;i++){
            for(int j = 0;j < 3;j++){
                for(int k = 0;k < 3;k++){
                    if(calc(calc(calc(a,b,i),c,j),d,k) == 10){
                        System.out.println("((("+a+" "+cms[i]+" "+b+") "+cms[j]+" "+c+") "+cms[k] + " " + d +")");
                        return 1;
                    }else if(calc(calc(a,calc(b,c,j),i),d,k) == 10){
                        System.out.println("(("+a+" "+cms[i]+" ("+b+" "+cms[j]+" "+c+")) "+cms[k] + " " + d +")");
                        return 1;
                    }else if(calc(calc(a,b,i),calc(c,d,k),j) == 10){
                        System.out.println("(("+a+" "+cms[i]+" "+b+") "+cms[j]+" ("+c+" "+cms[k] + " " + d +"))");
                        return 1;
                    }
                }
            }
        }
        return 0;
    }
     
    static int calc(int a,int b,int c){
        if(c == 0)return a+b;
        else if(c==1)return a-b;
        return a*b;
    }
     public static void main(String[] args) {
        while(true){
            int a[] = new int [4];
            
           for(int i=0;i<4;i++){
        	   a[i]=sc.nextInt();
           }
            if(a[0]+a[1]+a[2]+a[3]==0)break;
            int num = 0;
            for(int i = 0;i < 4;i++){
                for(int j = 0;j < 4;j++){
                    for(int k = 0;k < 4;k++){
                        for(int l = 0;l < 4;l++){
                            if(i == j || i == k || i == l || j == k || j == l || k == l)continue;
                            num = keisan(a[i],a[j],a[k],a[l]);
                            if(num == 1)break;
                        }
                        if(num == 1)break;
                    }
                    if(num == 1)break;
                }
                if(num == 1)break;
            }
            if(num == 0){
                System.out.println(0);
            }
        }
    }
 
}