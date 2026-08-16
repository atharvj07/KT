import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String line = input.readLine();
        Stack<Integer> s = new Stack<Integer>();
        int longest[] = new int[line.length()];
        int num = 1;
        int sub = 0;
        for (int i = 0 ; i<line.length() ; i++){
            if(line.charAt(i) == '(' ) {
                s.push(i);
                longest[i] = 0;
            }
            else{
                if(s.empty()){
                    longest[i] = 0;
                }
                else{
                    int spot = s.peek();
                    s.pop();
                    int length = i - spot + 1;
                    longest[i] = length;
                    if(spot > 0){
                        longest[i] = longest[i] + longest[spot - 1];
                    }
                }
            }
        }
        for(int i = 0; i<line.length(); i++){
            if(longest[i] == sub && sub != 0){
                num++;
            }
            else if(longest[i] > sub){
                sub = longest[i];
                num = 1;
            }
        }
        System.out.println(sub + " " + num);
    }
}