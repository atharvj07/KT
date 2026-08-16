import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
 

        while(sc.hasNext()){
        	String[] shikaku = new String[8];
        	for (int i = 0; i < 8; i++) {
        		shikaku[i] = sc.next();
        	}

        	int x = 0;
        	int y = 0;
        	boolean hakken = false;

        	for(int i = 0; i < 8; i++){
        		for (int j = 0; j < 8; j++) {
        			if(shikaku[i].charAt(j) == '1'){
        				x = j;
        				y = i;
        				hakken = true;
        				break;
        			}
        		}
        		if (hakken) {
        			break;
        		}
        	} 

        	if(x < 7 && y < 7){
        		if(shikaku[y].charAt(x+1) == '1' && shikaku[y+1].charAt(x) == '1' && shikaku[y+1].charAt(x+1) == '1'){
        			System.out.println("A");
        			continue;
        		}
        	}

        	if(x < 8 && y < 5){
        		if(shikaku[y+1].charAt(x) == '1' && shikaku[y+2].charAt(x) == '1' && shikaku[y+3].charAt(x) == '1'){
        			System.out.println("B");
        			continue;
        		}
        	}

        	if(x < 5 && y < 8){
        		if(shikaku[y].charAt(x+1) == '1' && shikaku[y].charAt(x+2) == '1' && shikaku[y].charAt(x+3) == '1'){
        			System.out.println("C");
        			continue;
        		}
        	}

        	if(x > 0 && y < 6){
        		if(shikaku[y+1].charAt(x-1) == '1' && shikaku[y+1].charAt(x) == '1' && shikaku[y+2].charAt(x-1) == '1'){
        			System.out.println("D");
        			continue;
        		}
        	}

        	if(x < 6 && y < 7){
        		if(shikaku[y].charAt(x+1) == '1' && shikaku[y+1].charAt(x+1) == '1' && shikaku[y+1].charAt(x+2) == '1'){
        			System.out.println("E");
        			continue;
        		}
        	}

        	if(x < 7 && y < 6){
        		if(shikaku[y+1].charAt(x) == '1' && shikaku[y+1].charAt(x+1) == '1' && shikaku[y+2].charAt(x+1) == '1'){
        			System.out.println("F");
        			continue;
        		}
        	}

        	System.out.println("G");

    	}
	}
}