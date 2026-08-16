import java.util.Scanner;

//High and Low Cube
public class Main{

	char[][][] s = {
			{{}},
			{
				"#######".toCharArray(),
				"#.....#".toCharArray(),
				"#...|.#".toCharArray(),
				"#.....#".toCharArray(),
				"#...|.#".toCharArray(),
				"#..-..#".toCharArray(),
				"#######".toCharArray()
			},
			{
				"#######".toCharArray(),
				"#..-..#".toCharArray(),
				"#...|.#".toCharArray(),
				"#..-..#".toCharArray(),
				"#.|...#".toCharArray(),
				"#..-..#".toCharArray(),
				"#######".toCharArray()
			},
			{
				"#######".toCharArray(),
				"#..-..#".toCharArray(),
				"#...|.#".toCharArray(),
				"#..-..#".toCharArray(),
				"#...|.#".toCharArray(),
				"#..-..#".toCharArray(),
				"#######".toCharArray()
			},
			{
				"#######".toCharArray(),
				"#.....#".toCharArray(),
				"#.|.|.#".toCharArray(),
				"#..-..#".toCharArray(),
				"#...|.#".toCharArray(),
				"#.....#".toCharArray(),
				"#######".toCharArray()
			},
			{
				"#######".toCharArray(),
				"#..-..#".toCharArray(),
				"#.|...#".toCharArray(),
				"#..-..#".toCharArray(),
				"#...|.#".toCharArray(),
				"#..-..#".toCharArray(),
				"#######".toCharArray()
			},
			{
				"#######".toCharArray(),
				"#..-..#".toCharArray(),
				"#.|...#".toCharArray(),
				"#..-..#".toCharArray(),
				"#.|.|.#".toCharArray(),
				"#..-..#".toCharArray(),
				"#######".toCharArray()
			},
			{
				"#######".toCharArray(),
				"#..-..#".toCharArray(),
				"#...|.#".toCharArray(),
				"#.....#".toCharArray(),
				"#...|.#".toCharArray(),
				"#.....#".toCharArray(),
				"#######".toCharArray()
			},
			{
				"#######".toCharArray(),
				"#..-..#".toCharArray(),
				"#.|.|.#".toCharArray(),
				"#..-..#".toCharArray(),
				"#.|.|.#".toCharArray(),
				"#..-..#".toCharArray(),
				"#######".toCharArray()
			},
			{
				"#######".toCharArray(),
				"#..-..#".toCharArray(),
				"#.|.|.#".toCharArray(),
				"#..-..#".toCharArray(),
				"#...|.#".toCharArray(),
				"#..-..#".toCharArray(),
				"#######".toCharArray()
			},
	};

	char[][] mirror_horizon(char[][] a){
		char[][] r = new char[7][7];
		for(int i=0;i<7;i++){
			for(int j=0;j<7;j++){
				r[i][j] = a[i][6-j];
			}
		}
		return r;
	}
	
	char[][] mirror_vertical(char[][] a){
		char[][] r = new char[7][7];
		for(int i=0;i<7;i++){
			for(int j=0;j<7;j++){
				r[i][j] = a[6-i][j];
			}
		}
		return r;
	}
	
	char[][] rotate270(char[][] a){
		char[][] r = new char[7][7];
		for(int i=0;i<7;i++){
			for(int j=0;j<7;j++){
				r[i][j] = a[6-j][i];
				if(r[i][j]=='-')r[i][j]='|';
				else if(r[i][j]=='|')r[i][j]='-';
			}
		}
		return r;
	}
	
	char[][] rotate90(char[][] a){
		char[][] r = new char[7][7];
		for(int i=0;i<7;i++){
			for(int j=0;j<7;j++){
				r[6-j][i] = a[i][j];
				if(r[6-j][i]=='-')r[6-j][i] = '|';
				else if(r[6-j][i]=='|')r[6-j][i]='-';
			}
		}
		return r;
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		int[][] me = {{0,7},{7,0},{7,7},{7,14},{7,21},{14,7}};
		int[][] foe = {{0,36},{7,29},{7,36},{7,43},{7,50},{14,36}};
		while(true){
			boolean end = false;
			char[][] map = new char[21][57];
			for(int i=0;i<21;i++){
				map[i] = sc.next().toCharArray();
				if(i==0&&map[i].length==1){
					end = true;break;
				}
			}
			if(end)break;
			int[] mine = new int[6];
			for(int k=0;k<6;k++){
				char[][] t = new char[7][7];
				for(int i=0;i<7;i++){
					for(int j=0;j<7;j++){
						t[i][j] = map[me[k][0]+i][me[k][1]+j];
					}
				}
				if(k==0){
					t = mirror_horizon(t);
				}
				else if(k==1){
					t = rotate270(t);
					t = mirror_horizon(t);
				}
				else if(k==2){
					t = mirror_horizon(t);
				}
				else if(k==3){
					t = rotate90(t);
					t = mirror_horizon(t);
				}
				else if(k==4){
					t = mirror_horizon(t);
				}
				else {
					t = mirror_horizon(t);
					t = mirror_vertical(t);
				}
				for(int x=1;x<10;x++){
					boolean f = true;
					for(int i=0;i<7;i++){
						for(int j=0;j<7;j++){
							if(s[x][i][j]!=t[i][j]){
								f = false;break;
							}
						}
					}
					if(f){
						mine[k] = x;
						break;
					}
				}
			}
			int[] oji = new int[6];
			for(int k=0;k<6;k++){
				char[][] t = new char[7][7];
				for(int i=0;i<7;i++){
					for(int j=0;j<7;j++){
						t[i][j] = map[foe[k][0]+i][foe[k][1]+j];
					}
				}
				if(k==0){
					t = mirror_horizon(t);
				}
				else if(k==1){
					t = rotate270(t);
					t = mirror_horizon(t);
				}
				else if(k==2){
					t = mirror_horizon(t);
				}
				else if(k==3){
					t = rotate90(t);
					t = mirror_horizon(t);
				}
				else if(k==4){
					t = mirror_horizon(t);
				}
				else {
					t = mirror_horizon(t);
					t = mirror_vertical(t);
				}
				for(int x=1;x<10;x++){
					boolean f = true;
					for(int i=0;i<7;i++){
						for(int j=0;j<7;j++){
							if(s[x][i][j]!=t[i][j]){
								f = false;break;
							}
						}
					}
					if(f){
						oji[k] = x;
						break;
					}
				}
			}
			int h = 0;
			int l = 0;
			for(int i=0;i<6;i++){
				for(int j=0;j<6;j++)
					if(mine[i]>oji[j])h++;
					else if(mine[i]<oji[j])l++;
			}
			System.out.println(h>=l?"HIGH":"LOW");
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}