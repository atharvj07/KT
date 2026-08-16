import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    
    Scanner sc = new Scanner(System.in);
    long H = sc.nextLong();
    long Attack = 0;
    long Monster = 1;
    
    while (H > 0) {
      Attack += Monster;
      H /= 2;
      Monster *= 2;
    }

    System.out.println(Attack);
    
  }
}