import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int d = sc.nextInt();
    
    int answer = 0;
    
    answer = n/(2*d+1);
    if(n%(2*d+1)!=0){
      answer=answer+1;
    }
    System.out.println(answer);
  }
  

  
}