import java.util.*;
public class Main{

     public static void main(String []args){
        
        Scanner sc=new Scanner(System.in);
        List<Integer> li=new ArrayList<Integer>();
        int x=sc.nextInt();
        int y=sc.nextInt();
        for(int i=0;i<y;i++)
        li.add(sc.nextInt());
        for(int i=0;i<=x;i++)
        {
            int sub=x-i;
            int add=x+i;
            if(!(li.contains(sub) )){
                
              System.out.println(sub);
              System.exit(0);}
            if(!( li.contains(add))){
               System.out.println(add);
               System.exit(0);}
        }
       System.out.println("-1");  
     }
}