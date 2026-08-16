import java.util.*;
public class Main{
	public static void main(String[] args){
    	Scanner sc = new Scanner(System.in);
      char[] c = sc.next().toCharArray();
      int cnt = 0;
      for(int i = 0;i < c.length-1;i++){
      	if(c[i]!=c[i+1])cnt++;
      }
      System.out.println(cnt);
    }
}
