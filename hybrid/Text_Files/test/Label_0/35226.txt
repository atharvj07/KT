import java.util.Scanner;

/**
 * Created by Reopard on 2014/06/05.
 */
public class Main{

    static Scanner sc = new Scanner(System.in);
    static Position[] direction = {new Position(-1, 0), new Position(0, -1), new Position(1, 0), new Position(0, 1)};

    public static void main(String args[]){
        int N, number, tmp_dire, right, left, top, bottom;
        Position[] square_pos;
        while((N = sc.nextInt()) != 0){
            right = 0;
            left = 0;
            top = 0;
            bottom = 0;
            square_pos = new Position[N];
            square_pos[0] = new Position(0, 0);
            for(int i = 1; i < N; i++){
                number = sc.nextInt();
                tmp_dire = sc.nextInt();
                square_pos[i] = new Position(square_pos[number].x, square_pos[number].y);
                square_pos[i].movePosition(direction[tmp_dire]);
            }
            for(int j = 0; j < square_pos.length; j++){
                if(square_pos[j].x < left) left = square_pos[j].x;
                else if(square_pos[j].x > right) right = square_pos[j].x;
                if(square_pos[j].y < bottom) bottom = square_pos[j].y;
                else if(square_pos[j].y > top) top = square_pos[j].y;
            }
            System.out.println((right - left +1) + " " + (top - bottom + 1));
        }
    }

    static class Position{
        int x, y;

        Position(int x, int y){
            this.x = x;
            this.y = y;
        }

        void movePosition(Position tmp){
            x += tmp.x;
            y += tmp.y;
        }
    }
}