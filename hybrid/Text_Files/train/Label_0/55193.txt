
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class TC
{
    static int n, h;
    static Pair[] arr;
    static long good;

    
    static boolean solve() // true for original, false for shifts
    {
        Arrays.sort( arr );
        
        // find cost in single array
        
        long min1 = arr[ 0 ].first + arr[ 1 ].first;
        long max1 = arr[ arr.length-1 ].first + arr[ arr.length-2 ].first;
        long DIFF1 = max1 - min1;
        
        if( arr.length == 2 )
        {
            return true;
        }
        
        // Move lowest to other array
        
       ArrayList<Integer> cost = new ArrayList();
       
       cost.add( arr[ 0 ].first + arr[ 1 ].first + h );
       cost.add( arr[ 1 ].first + arr[ 2 ].first );
       cost.add( arr[ 0 ].first + arr[ arr.length-1 ].first + h );
       cost.add( arr[ arr.length-1 ].first + arr[ arr.length-2 ].first  );
       
       long MIN = Long.MAX_VALUE;
       long MAX = -1;
       
       for( int i=0; i<4; i++ )
       {
           int c= cost.get( i );
           MIN = Math.min( c, MIN );
           MAX = Math.max( c, MAX );
       }
       
       long DIFF2 = MAX - MIN;
       
       if( DIFF1 <= DIFF2 )
       {
           good = DIFF1;
           return true;
       }
   
       good = DIFF2;
       return false;
       
    }
    
    static void print( boolean isOrig )
    {
        System.out.println( good );
        int minIndex = arr[ 0 ].second;
        
        if( isOrig )
        {
            for( int i=0; i<arr.length; i++ )
                System.out.print("1 ");
            
            System.out.println();
            return;
        }
        
        for( int i=0; i<n; i++ )
        {
            if( i != minIndex )
                System.out.print("1 ");
            
            else
                System.out.print("2 ");
        }
        
        System.out.println();
        return;
    }
    public static void main( String[] args ) throws IOException
    {
        BufferedReader br = new BufferedReader( new InputStreamReader( System.in ));
        
        String s = br.readLine();
        StringTokenizer tok = new StringTokenizer(s );
        
        n = Integer.parseInt( tok.nextToken() );
        h = Integer.parseInt( tok.nextToken() );
        
        s = br.readLine();
        tok = new StringTokenizer(s );
        
        arr = new Pair[ n ];
        
        for( int i=0; i<n; i++ )
            arr[ i ] = new Pair( Integer.parseInt( tok.nextToken() ), i );
        
        boolean isOrig = solve();
        print( isOrig );
    }
}


class Pair implements Comparable
{
    int first, second; // first -> primary key for sorting/comparison
    
    public Pair( int _x1, int _x2 )
    {
        first = _x1;
        second = _x2;
    }
    
    public int compareTo( Object o )
    {
        Pair n = ( Pair ) o ;
        
        if( first != n.first )
            return first-n.first;
        
        else
            return second-n.second;
    }
    
    public int hashCode() // Always check for equality after retrieving from hashtable to detect collisions ! 
    {
        int result = 23;
        result = 31*result + first;
        result = 31*result + second;
        return result;
        
    }
    
    public boolean equals( Object o )
    {
        Pair p = ( Pair ) o;
        
        if( first == p.first )
            if( second == p.second )
                return true;
        
        return false;
    }
    
    
}


