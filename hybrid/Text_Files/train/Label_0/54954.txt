import java.util.*;
public class Main {
    int runner;
    int cnt = 0;
    int cnt2 = 0;
    String time;
    Player pArray[][] = new Player[3][8];
    Player rank[] = new Player[8];
    Player otherArray[] = new Player[18];
	private Scanner sc;
    void doIt(){
        sc = new Scanner(System.in);
        for(int i = 0; i < 3; i++){
        	for(int k = 0; k < 8; k++){
        		runner = sc.nextInt();
        		time = sc.next();
        		pArray[i][k] = new Player(runner,time);
        	}
        }
        for(int i = 0; i < pArray.length; i++){
			Arrays.sort(pArray[i]);
			Arrays.toString(pArray[i]);
			rank[cnt] = pArray[i][0];
			cnt++;
			rank[cnt] = pArray[i][1];
			cnt++;
			for(int k = 2; k < 8; k++){
				otherArray[cnt2] = pArray[i][k];
				cnt2++;
			}
        }
        Arrays.sort(otherArray);
        rank[6] = otherArray[0];
        rank[7] = otherArray[1];
        for(int i = 0; i < rank.length; i++){
        	System.out.println(rank[i].pnumber + " " + rank[i].time);
        }
    }
    class Player implements Comparable<Player>{
        int pnumber;
        String time;
        Player(int pnumber,String time){
            this.pnumber = runner;
            this.time = time;
        }
        @Override
        public String toString(){
        	return pnumber + " " + time;
        }
        @Override
        public int compareTo(Player p){
            return this.time.compareTo(p.time);
        }
    }
    public static void main(String[] args) {
        new Main().doIt();
    }
}