import java.util.*;

public class Main{
	public static void main(String[] args){
    	Scanner sc = new Scanner(System.in);
      	int X = Integer.parseInt(sc.next());
     	int Y = Integer.parseInt(sc.next());
      	
      	char S[][] = new char[50][50];
      
      	for(int x = 0; x < X;  x++){
          	String s = sc.next();
        	for(int y = 0; y < Y; y++){
            	S[x][y] = s.charAt(y);
           	}
        }
      //System.out.println(Arrays.deepToString(S));
      int dx[] = {1, 1, 0, -1, -1, -1, 0, 1};
      int dy[] = {0, 1, 1, 1, 0, -1, -1, -1};
      
      for(int i = 0; i < X;  i++){
        	for(int j = 0; j < Y; j++){
            	if(S[i][j] == '.'){
                	int count = 0;
                  	for(int k = 0; k < 8; k++){
                    	int x = i + dx[k];
                      	int y = j + dy[k];
                      	if(0 <= x && x < X && 0 <= y && y < Y && S[x][y] == '#'){
                        	count++;
                        }
                      S[i][j] = (char)('0' + count);
                    }
                }
           	}
      }
        for(int i = 0; i < X; i++){
        	for(int j = 0; j < Y; j++){
            	System.out.print(S[i][j]);
            }
          System.out.println();
        }
    }
}