import java.util.*;

class Main{
  public static void main (String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int M = sc.nextInt();
    Integer Array[] = new Integer[N];
    boolean AC[] = new boolean[N];
    for(int i=0;i<N;i++){
      Array[i] = 0;
      AC[i] = false;
    }
    for (int i=0;i<M;i++){
     int p = sc.nextInt();
     String s = sc.next();
     if (s.equals("WA")){
      if (AC[p-1] == false){
        Array[p-1] += 1;
      }
     }else{
       AC[p-1] = true;
     }
    }
    int one = 0;
    int two = 0;
    for (int i=0;i<N;i++){
      if (AC[i]){
        one += 1;
        two += Array[i];
      }
    }
    System.out.print(one);
    System.out.print(" ");
    System.out.print(two);
    
    

  }
}