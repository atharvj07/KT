import java.util.Scanner;

public class Main{
public static void main(String[] args){
  Scanner sc = new Scanner(System.in);
int N = sc.nextInt();
int answer = 0;
if(N>=3*5*7){
  answer++;
}
if(N>=3*5*11){
  answer++;
}
if(N>=3*5*13){
  answer++;
}
if(N>=3*3*3*5){
  answer++;
}
if(N>=3*3*3*7){
  answer++;
}

System.out.println(answer);
}
}
