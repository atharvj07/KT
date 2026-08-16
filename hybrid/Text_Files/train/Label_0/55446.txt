import java.util.Scanner;

public class JavaApplication29 {

   
    public static void main(String[] args){
        Scanner input=new Scanner(System.in);
        int count=0,n;
        n=input.nextInt();
        String x;
        x=input.next();
        
        
        if(n==x.length() ){
        for(int i=0;i<x.length();i=i+count){
            count++;
            System.out.print(x.charAt(i));
            
        }
        }
    }
    
}