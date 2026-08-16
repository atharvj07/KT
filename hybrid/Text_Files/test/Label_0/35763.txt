import java.util.Scanner;

class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int n = Integer.parseInt(sc.next());
    int[] numbers = new int[n];
    
    int ave_1 = 0;
    int ave_2 = 0;
    for(int i=0; i<n; i++){
      numbers[i] = Integer.parseInt(sc.next());
      ave_1 += numbers[i];
      ave_2 += numbers[i];
    }
    ave_1 /= n;
    ave_2 /= n;
    ave_2++;
    
    int judge_1 = 0;
    int judge_2 = 0;
    for(int j=0; j<n; j++){
      judge_1 += (numbers[j]-(ave_1))*(numbers[j]-(ave_1));
      judge_2 += (numbers[j]-(ave_2))*(numbers[j]-(ave_2));
    }
    
    System.out.println(Math.min(judge_1, judge_2));
  }
}