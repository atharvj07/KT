import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int numStep = sc.nextInt();
        int multiple = sc.nextInt();
        int answer = 0;
        if(numStep<multiple){
            System.out.println(-1);
        }
        else{
            if(numStep%2==0){
                answer = numStep/2;
            }
            else{
                answer = (numStep+1)/2;
            }
            if(answer%multiple ==0){
                System.out.println(answer);
            }
            else{
                while(answer%multiple!=0){
                    answer = answer+1;
                }
                System.out.println(answer);
            }
        }
        
    }
}
            
  