import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] input = sc.next().toCharArray();
        int k = sc.nextInt();
        int index = 0;
        while(k > 0 && index < input.length){
            int diff = input[index] - 'a';
            if(diff == 0){
                
            }else if(diff + k >= 26){
                input[index] = 'a';
                k = k - (26 - diff);
            }
            index += 1;
        }
        index = input.length - 1;
        input[index] = (char) (((input[index] - 'a' + k) % 26) + 'a');
        String result = new String(input);
        System.out.println(result);
    }
}