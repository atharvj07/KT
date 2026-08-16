import java.util.*;
class Main{
    public static void mktable(short[] dice, short[][] table){
        table[0][0] = dice[1];
        table[0][1] = dice[2];
        table[0][2] = dice[4];
        table[0][3] = dice[3];

        table[1][0] = dice[0];
        table[1][1] = dice[3];
        table[1][2] = dice[5];
        table[1][3] = dice[2];

        table[2][0] = dice[0];
        table[2][1] = dice[1];
        table[2][2] = dice[5];
        table[2][3] = dice[4];

        table[3][0] = dice[0];
        table[3][1] = dice[4];
        table[3][2] = dice[5];
        table[3][3] = dice[1];

        table[4][0] = dice[0];
        table[4][1] = dice[2];
        table[4][2] = dice[5];
        table[4][3] = dice[3];

        table[5][0] = dice[1];
        table[5][1] = dice[3];
        table[5][2] = dice[4];
        table[5][3] = dice[2];
    }
    public static boolean check(short[] dice, short[] dice2, short[][] table){
        int top, k; 
        for(top = 0; top < 6; top++){
            if(dice2[0] == dice[top]){
                for(k = 0; k < 4; k++){
                    if(dice2[1] == table[top][k]){
                        if(dice2[2] == table[top][(k+1)%4]){
                            if(dice2[4] == table[top][(k+2)%4]){
                                if(dice2[3] == table[top][(k+3)%4]){
                                    if(dice2[5] == dice[5-top]){
                                        System.out.println("No");
                                        System.exit(0);
                                   }
                                }
                            }   
                        }
                    }
                }
            }
        }
        return false;
    }


    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        short[][] dice_t = new short[100][6];
        short[][][] table = new short[100][6][4];

        short n = scanner.nextShort();
        for(short i = 0; i < n; i++){
            for(short j = 0; j < 6; j++)dice_t[i][j] = scanner.nextShort();
            mktable(dice_t[i], table[i]);
            for(short j = 0; j < i; j++){
                if(check(dice_t[j], dice_t[i], table[j])){
                    System.out.println("No");
                    System.exit(0);
                }
            }
        }
        System.out.println("Yes");
    }
}

