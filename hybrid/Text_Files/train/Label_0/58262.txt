import java.util.Arrays;
import java.util.Scanner;

public class Main 
{
	static boolean debug = false;
	static int[][] input = new int[5][5];
	static int[][][] nets = 
		{
			{{1,2,1,0,0},
			 {0,3,0,0,0},
			 {0,2,0,0,0},
			 {0,3,0,0,0}},
			
			{{1,2,0,0,0},
			 {0,3,1,0,0},
			 {0,2,0,0,0},
			 {0,3,0,0,0}},
			
			{{1,2,0,0,0},
			 {0,3,0,0,0},
			 {0,2,1,0,0},
			 {0,3,0,0,0}},
				
			{{1,2,0,0,0},
			 {0,3,0,0,0},
			 {0,2,0,0,0},
			 {0,3,1,0,0}},
			
			{{2,0,0,0,0},
			 {1,3,1,0,0},
			 {0,2,0,0,0},
			 {0,3,0,0,0}},
			
			{{3,0,0,0,0},
			 {1,2,0,0,0},
			 {0,3,1,0,0},
			 {0,2,0,0,0}},
			
			{{3,0,0,0,0},
			 {2,1,0,0,0},
			 {0,3,0,0,0},
			 {0,1,2,0,0}},				
			
			{{3,2,0,0,0},
			 {0,1,3,0,0},
			 {0,0,2,1,0},
			 {0,0,0,0,0}},
			
			{{0,3,0,0,0},
			 {1,2,1,0,0},
			 {0,3,0,0,0},
			 {0,2,0,0,0}},
				
			{{0,3,0,0,0},
			 {1,2,0,0,0},
			 {0,3,1,0,0},
			 {0,2,0,0,0}},				
				
			{{1,2,1,0,0},
			 {0,0,3,2,3},
			 {0,0,0,0,0},
			 {0,0,0,0,0}},				
			
			//Flipped ones

			{{0,2,1,0,0},
			 {1,3,0,0,0},
			 {0,2,0,0,0},
			 {0,3,0,0,0}},
			
			{{0,2,1,0,0},
			 {0,3,0,0,0},
			 {1,2,0,0,0},
			 {0,3,0,0,0}},
				
			{{0,2,1,0,0},
			 {0,3,0,0,0},
			 {0,2,0,0,0},
			 {1,3,0,0,0}},
			
			{{0,0,2,0,0},
			 {1,3,1,0,0},
			 {0,2,0,0,0},
			 {0,3,0,0,0}},
			
			{{0,0,3,0,0},
			 {0,2,1,0,0},
			 {1,3,0,0,0},
			 {0,2,0,0,0}},
			
			{{0,0,3,0,0},
			 {0,1,2,0,0},
			 {0,3,0,0,0},
			 {2,1,0,0,0}},				
			
			{{0,0,2,3,0},
			 {0,3,1,0,0},
			 {1,2,0,0,0},
			 {0,0,0,0,0}},
			
			{{0,3,0,0,0},
			 {0,2,1,0,0},
			 {1,3,0,0,0},
			 {0,2,0,0,0}},				
				
			{{0,0,1,2,1},
			 {3,2,3,0,0},
			 {0,0,0,0,0},
			 {0,0,0,0,0}},					
		};
	
	static void printout()
	{
		if(!debug) {return;}
		for(int y = 0; y <= 4; y++)
		{
			for(int x = 0; x <= 4; x++)
			{
				System.out.print(input[y][x] + " ");
			}
			System.out.println("");
		}		
	}
	
	static void rotate()
	{
		int[][] temp = new int[5][5];
		for(int y = 0; y < 5; y++)
		{
			for(int x = 0; x < 5; x++)
			{
				temp[y][x] = input[4-x][y];
			}
		}
		
		for(int y = 0; y < 5; y++)
		{
			for(int x = 0; x < 5; x++)
			{
				input[y][x] = temp[y][x];
			}
		}
		gotopleft();
	}
	
	static void gotopleft()
	{
		//go left
		boolean goleft = true;
		
		while(goleft)
		{
			for(int y = 0; y < 5; y++)
			{
				if(input[y][0] != 0)
				{
					goleft = false;
				}
			}
			
			if(goleft)
			{ //all 0s on the left
				for(int x = 0; x < 5; x++)
				{
					for(int y = 0; y < 5; y++)
					{
						if(x < 4)
						{
							input[y][x] = input[y][x+1];
						}
						else
						{ //remove the last ones
							input[y][x] = 0;
						}
					}
				}
			}
		}
		
		//go top
		boolean gotop = true;
		
		while(gotop)
		{
			for(int x = 0; x < 5; x++)
			{
				if(input[0][x] != 0)
				{
					gotop = false;
				}
			}
			
			if(gotop)
			{ //all 0s on the top
				for(int y = 0; y < 5; y++)
				{
					for(int x = 0; x < 5; x++)
					{
						if(y < 4)
						{
							input[y][x] = input[y+1][x];
						}
						else
						{ //remove the last ones
							input[y][x] = 0;
						}
					}
				}
			}
		}
	}
	
	static boolean checkall()
	{
		gotopleft();
		
		for(int i = 0; i < 20; i++)
		{
			if(shapeexactlymatches(i)) {return true;}
			rotate();
			if(shapeexactlymatches(i)) {return true;}
			rotate();
			if(shapeexactlymatches(i)) {return true;}
			rotate();
			printout();
			if(shapeexactlymatches(i)) {return true;}
		}
		return false;
	}
		
	static boolean shapeexactlymatches(int netid)
	{ //net, y, x
		int[][] net = nets[netid];
		int[] pairfirstnumber = new int[3];
		int matched = 0;
		for(int y = 0; y <= 3; y++)
		{
			for(int x = 0; x <= 4; x++)
			{
//				System.out.println(x + "," +y + ": " + net[y][x]);
				
				if((input[y][x] == 0)^(net[y][x] == 0))
				{
					if(debug)System.out.println("Mismatch quit: " + x + " " + y);
					return false;
				}
				else
				{
					if(input[y][x] > 0)
					{
						int curPair = net[y][x]-1;
						if(pairfirstnumber[curPair] == 0)
						{ //first number of the pair
							pairfirstnumber[curPair] = input[y][x];
						}
						else
						{ //second number of the pair
							if(input[y][x] + pairfirstnumber[curPair] == 7)
							{ //good pair!
							}
							else
							{
								if(debug)System.out.println("There was no love. Pair: " + curPair + " Pairants: " + pairfirstnumber[curPair] + " and " + input[y][x] );
								return false;
							}
						}
						
						matched += 1;
	//					System.out.println("Matching: " + x + " " + y);
						if(matched >= 6)
						{
							if(debug)System.out.println("Sixth match at: " + x + " " + y);
							return true;
						}
					}
				}
			}
		}
		return false;
	}
	
	public static void main(String[] args) 
	{
//		System.out.println("Ey");
		int[][] net = nets[2];
//		System.out.println(net[0][1]);
//		System.out.println(nets[2][0][1]);
		Scanner scan = new Scanner(System.in);
		


		int n = scan.nextInt();
		
		for(int i = 0; i < n; i++)
		{
			boolean preout = false;
			boolean[] numberappeared = new boolean[6];
			input = new int[5][5];
			for(int y = 0; y <= 4; y++)
			{
				for(int x = 0; x <= 4; x++)
				{
					input[y][x] = scan.nextInt();
					
					int cur = input[y][x];
					
					if(!preout)
					{
						if(cur < 0 || cur > 6)
						{
							preout = true;
						}
						else
						{
							if(cur > 0)
							{ //valid number
								if(numberappeared[cur-1])
								{
									preout = true;
								}
								else
								{
									numberappeared[cur-1] = true;
								}
							}
						}
					}
				}
			}
			
			
//			rotate();
//			printout();

			//
//			gotopleft();
//			rotate();
//			printout();
//			shapeexactlymatches(0);
			
			if(!preout)
			{
				System.out.println(checkall());
			}
			else
			{
				System.out.println("false");
			}
		}
	}
}

