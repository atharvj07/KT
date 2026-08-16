import java.util.*;

public class Main {
    

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
       
        int N = sc.nextInt();int c=0,i=0;boolean flag=false;
        for(int x=1;x<=N;++x){
            int a=sc.nextInt();
            int b=sc.nextInt();//String s1="",s2="";
            
            if(b-a==0){
                if(i==x || i+1==x){
                    c++;i=x;
                    }
                
            }
            else{
                i=x;c=0;
            }
            if(c==3){
                flag=true;
                break;
            }
        }
            if(flag){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
        
    
    }
}