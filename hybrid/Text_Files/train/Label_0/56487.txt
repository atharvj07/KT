import java.util.ArrayDeque;
import java.util.Scanner;
import java.util.Stack;

public class Main
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int testCase = sc.nextInt();
        for (int g=0;g<testCase;g++) {
            StringBuilder sb = new StringBuilder();
            Stack<Integer> stack = new Stack<Integer>();
            int huuu = sc.nextInt();
            int[] gyuet = new int[huuu];
            for(int i=0;i<huuu;i++)
                gyuet[i] = sc.nextInt();
            int[] fuut = new int[huuu];
            int indx=huuu-1;
            for(int i=0;i<huuu;i++){
                if(!stack.isEmpty()){
                    if(stack.firstElement()<gyuet[i])
                        while(!stack.isEmpty()) {
                            fuut[indx] = stack.pop();
                            indx--;
                        }
                }
                stack.push(gyuet[i]);
            }
            while(!stack.isEmpty()){
                fuut[indx] = stack.pop();
                indx--;
            }
            for(int u=0;u<huuu;u++)
                sb.append(fuut[u]).append(" ");
            System.out.println(sb);
        }
    }
}