import java.util.*;

public class Main {
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int[] num = new int[9];
    
    for(int i=0; i<9; i++){
        num[i] = sc.nextInt();
    }
    if(num[0]-num[3]==num[1]-num[4] && num[2]-num[5]==num[1]-num[4] && num[0]-num[3]==num[2]-num[5]){
      if(num[0]-num[6]==num[1]-num[7] && num[2]-num[8]==num[1]-num[7] && num[0]-num[6]==num[2]-num[8]){
        if(num[3]-num[6]==num[4]-num[7] && num[5]-num[8]==num[4]-num[7] && num[3]-num[6]==num[5]-num[8]){
          System.out.println("Yes");
        }else{
          System.out.println("No");
        }
      }else{
          System.out.println("No");
        }
    }else{
          System.out.println("No");
        }
    //System.out.println(count);
  }
}