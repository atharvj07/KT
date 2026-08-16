import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    String s = sc.next();
    int n = s.length();
    int answer=0;
    for(int i=0;i<n/2;i++){
      if(s.substring(i,i+1).equals(s.substring(n-i-1,n-i))){
        answer=answer+0;
      }else{
        answer=answer+1;
      }
    }
    System.out.println(answer);
  }
  

  
}