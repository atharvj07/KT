
import java.io.*;
import java.util.*;



public class Main {
	int W, D;
	char[][] field;
	String col;
	
	class State{
		int x;
		int y;
		Dice<Character> dice;
		int idx;
		int d;
		public State(int x, int y, Dice<Character> dice, int idx, int d){
			this.x = x;
			this.y = y;
			this.dice = dice;
			this.idx = idx;
			this.d = d;
		}
		public boolean equals(Object o){
			if(o != null && o instanceof State){
				State d = (State)o;
				return d.x == x && d.y == y && d.idx == idx && d.dice.equalsDirection(dice);
			}else{
				return false;
			}
		}
		public int hashCode(){
			return Objects.hash(x, y, dice.getId(Dice.TOP), dice.getId(Dice.EAST));
		}
		public String toString(){
			return String.format("[(%d,%d),%d,%d, %s]", x, y, idx, d, dice.toString());
		}
	}
	
	public void solve() {
		while(true){
			W = nextInt();
			D = nextInt();
			if(W == 0) break;
			
			field = new char[D + 2][W + 2];
			int sx = 0, sy = 0;
			for(int i = 1; i <= D; i++){
				String str = next();
				for(int j = 1; j <= W; j++){
					switch(str.charAt(j - 1)){
					case '#':
						sx = j;
						sy = i;
					case 'w':
						field[i][j] = 1;
						break;
					case 'k':
						field[i][j] = 0;
						break;
					default:
						field[i][j] = str.charAt(j - 1);	
					}
				}
			}
			col = next();
			State s = new State(sx, sy, new Dice<Character>('r', 'c', 'g', 'm', 'b', 'y'), 0, 0);
			HashSet<State> reach = new HashSet<>();
			Queue<State> queue = new ArrayDeque<>();
			queue.add(s);
			int ans = -1;
			while(!queue.isEmpty()){
				s = queue.poll();
				if(!reach.contains(s)){
					char c = field[s.y][s.x];
					if(c == 1 ||
							(c == col.charAt(s.idx) &&
							field[s.y][s.x] == c &&
							c == s.dice.getTop())){
						reach.add(s);
						int ni = s.idx;
						if(c != 1){
							ni++;
							if(ni == 6){
								ans = s.d;
								break;
							}
						}
						queue.add(new State(s.x + 1, s.y, s.dice.rollEast(), ni, s.d + 1));
						queue.add(new State(s.x, s.y - 1, s.dice.rollNorth(), ni, s.d + 1));
						queue.add(new State(s.x - 1, s.y, s.dice.rollWest(), ni, s.d + 1));
						queue.add(new State(s.x, s.y + 1, s.dice.rollSouth(), ni, s.d + 1));
						
					}
				}
			}
			if(ans == -1){
				out.println("unreachable");
			}else{
				out.println(ans);
			}
		}
	}
	
	private static PrintWriter out;

	public static void main(String[] args) {
		out = new PrintWriter(System.out);
		new Main().solve();
		out.flush();
	}

	public static int nextInt() {
		int num = 0;
		String str = next();
		boolean minus = false;
		int i = 0;
		if(str.charAt(0) == '-'){
			minus = true;
			i++;
		}
		int len = str.length();
		for(; i < len; i++){
			char c = str.charAt(i);
			if(!('0' <= c && c <= '9')) throw new RuntimeException();
			num = num * 10 + (c - '0');
		}
		return minus ? -num : num;
	}

	public static long nextLong() {
		long num = 0;
		String str = next();
		boolean minus = false;
		int i = 0;
		if(str.charAt(0) == '-'){
			minus = true;
			i++;
		}
		int len = str.length();
		for(; i < len; i++){
			char c = str.charAt(i);
			if(!('0' <= c && c <= '9')) throw new RuntimeException();
			num = num * 10l + (c - '0');
		}
		return minus ? -num : num;
	}

	public static String next() {
		int c;
		while(!isAlNum(c = read())){}
		StringBuilder build = new StringBuilder();
		build.append((char)c);
		while(isAlNum(c = read())){
			build.append((char)c);
		}
		return build.toString();
	}

	private static byte[] inputBuffer = new byte[1024];
	private static int bufferLength = 0;
	private static int bufferIndex = 0;

	private static int read() {
		if(bufferLength < 0) throw new RuntimeException();
		if(bufferIndex >= bufferLength){
			try{
				bufferLength = System.in.read(inputBuffer);
				bufferIndex = 0;
			}catch(IOException e){
				throw new RuntimeException(e);
			}
			if(bufferLength <= 0) return(bufferLength = -1);
		}
		return inputBuffer[bufferIndex++];
	}

	private static boolean isAlNum(int c) {
		return '!' <= c && c <= '~';
	}
}


class Dice<T> {
	public static final int TOP = 0;
	public static final int BOTTOM = 5;
	public static final int EAST = 4;
	public static final int WEST = 1;
	public static final int NORTH = 3;
	public static final int SOUTH = 2;
	
	private final int[] id = new int[6];
	private final ArrayList<T> values;
	
	public Dice(){
		values = new ArrayList<>(6);
		for(int i = 0; i < 6; i++){
			id[i] = i;
			values.add(null);
		}
	}
	
	public Dice(T top, T bottom, T north, T south, T east, T west){
		this();
		values.set(TOP, top);
		values.set(BOTTOM, bottom);
		values.set(EAST, east);
		values.set(WEST, west);
		values.set(NORTH, north);
		values.set(SOUTH, south);
	}
	
	private Dice(Dice<T> d){
		values = d.values;
		for(int i = 0; i < 6; i++){
			id[i] = d.id[i];
		}
	}

	public Dice<T> rollNorth(){
		return roll(TOP, SOUTH, BOTTOM, NORTH);
	}
	public Dice<T> rollSouth(){
		return roll(TOP, NORTH, BOTTOM, SOUTH);
	}
	public Dice<T> rollWest(){
		return roll(TOP, EAST, BOTTOM, WEST);
	}
	public Dice<T> rollEast(){
		return roll(TOP, WEST, BOTTOM, EAST);
	}
	public Dice<T> rollClockWise(){
		return roll(NORTH, WEST, SOUTH, EAST);
	}
	public Dice<T> rollCounterClockWise(){
		return roll(NORTH, EAST, SOUTH, WEST);
	}
	
	public T getTop(){
		return values.get(id[TOP]);
	}
	
	public int getId(int face){
		return id[face];
	}
	
	
	public boolean equalsDirection(Dice<T> d){
		return d.getId(TOP) == getId(TOP) && d.getId(EAST) == getId(EAST);
	}

	public String toString(){
		StringBuilder build = new StringBuilder();
		build.append("TOP:");
		build.append(values.get(id[TOP]));
		build.append(",BOTTOM:");
		build.append(values.get(id[BOTTOM]));
		build.append(",NORTH:");
		build.append(values.get(id[NORTH]));
		build.append(",SOUTH:");
		build.append(values.get(id[SOUTH]));
		build.append(",WEST:");
		build.append(values.get(id[WEST]));
		build.append(",EAST:");
		build.append(values.get(id[EAST]));
		return build.toString();
	}
	private Dice<T> roll(int a, int b, int c, int d){
		Dice<T> nd = new Dice<T>(this);
		int tmp = nd.id[a];
		nd.id[a] = nd.id[b];
		nd.id[b] = nd.id[c];
		nd.id[c] = nd.id[d];
		nd.id[d] = tmp;
		return nd;
	}
}