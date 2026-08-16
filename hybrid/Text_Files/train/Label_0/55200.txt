import java.util.Scanner;

public class problem15 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        char[][] c = new char[4][4];
        for(int i = 0; i < 4; i++){
            String temp = input.next();
            for(int j = 0; j < 4; j++){
                c[i][j] = temp.charAt(j);
            }
        }
        String result = "NO";
        outer : for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                if((c[i][j] == c[i][j+1] && c[i][j] == c[i+1][j])
                        || (c[i][j] == c[i][j+1] && c[i][j] == c[i+1][j+1])
                        || (c[i][j] == c[i+1][j] && c[i][j] == c[i+1][j+1])
                        || (c[i+1][j] == c[i+1][j+1] && c[i+1][j] == c[i][j+1] && c[i+1][j+1] == c[i][j+1])){
                    result = "YES";
                    break outer;
                }
            }
        }
        System.out.println(result);
    }
}