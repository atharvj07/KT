import java.util.*;
public class Main {
    public static void main(String[] args) throws java.io.IOException{
        Scanner scan = new Scanner(System.in);

        while(true){
        int n= scan.nextInt();
        if(n==0)break;
       
        int max =0;
        int min =501;
        while(n!=0){
        	int sum =0;
        	for(int i=0;i<5;i++)
        		sum+=scan.nextInt();
        	max=Math.max(max,sum);
        	min = Math.min(min, sum);
        	n--;
        }
        System.out.println(max+" "+min);
        }
    }
}