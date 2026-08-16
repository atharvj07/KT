import java.util.Scanner;

public class Main {
	Scanner sc;
	int[][] map;
	final int WIDTH  = 12;
	final int HEIGHT = 12;

	private Main(){
		sc = new Scanner( System.in );
	}

	private void visit( int x, int y ){
		if( x < 0 || y < 0 || x >= WIDTH || y >= HEIGHT || map[ x ][ y ] == 0){ return; }
		map[ x ][ y ] = 0;
		visit( x - 1, y     );
		visit( x    , y - 1 );
		visit( x    , y + 1 );
		visit( x + 1, y     );

	}

	private void run(){
		while( sc.hasNext() ){
			int counter = 0;
			map = new int[ WIDTH ][ HEIGHT ];
			for( int y = 0; y < HEIGHT; y++ ){
				String line = sc.next();
				char[] cline = line.toCharArray();
				for(int x = 0; x < WIDTH; x++ ){
					map[ x ][ y ] = cline[ x ] - '0';
				}
			}
			for( int y = 0; y < HEIGHT; y++ ){
				for( int x = 0; x < WIDTH; x++ ){
					if( map[ x ][ y ] == 1 ){
						counter++;
						visit( x, y );
					}
				}
			}
			System.out.println( counter );
		}
	}

	public static void main( String[] args ){
		new Main().run();
	}

}