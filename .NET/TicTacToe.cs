using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Project1
{
    internal class TicTacToe
    {
        static char[,] playField =
        {
            {'1','2','3' },
            {'4','5','6' },
            {'7','8','9' }

        };

        

        static int turns = 0;

        public static void Main(String[] args)
        {
            int player = 2;
            int input = 0;
            bool inputCorrect = true;


            do
            {

                if (player == 2)
                {
                    player = 1;
                    EnterXorO(player, input);
                }
                else
                {
                    player = 2;
                    EnterXorO(player, input);
                }

                SetField();

                char[] playerChars = { 'X', 'O' };
                foreach (char playerChar in playerChars)
                {
                    if (((playField[0, 0] == playerChar) && (playField[0, 1] == playerChar) &&  (playField[0, 2] == playerChar))
                        || ((playField[1, 0] == playerChar) && (playField[1, 1] == playerChar) && (playField[1, 2] == playerChar))
                        || ((playField[2, 0] == playerChar) && (playField[2, 1] == playerChar) && (playField[2, 2] == playerChar))
                        || ((playField[0, 0] == playerChar) && (playField[1, 0] == playerChar) && (playField[2, 0] == playerChar))
                        || ((playField[0, 1] == playerChar) && (playField[1, 1] == playerChar) && (playField[2, 1] == playerChar))
                        || ((playField[0, 2] == playerChar) && (playField[1, 2] == playerChar) && (playField[2, 2] == playerChar))
                        || ((playField[0, 0] == playerChar) && (playField[1, 1] == playerChar) && (playField[2, 2] == playerChar))
                        || ((playField[0, 2] == playerChar) && (playField[1, 1] == playerChar) && (playField[2, 0] == playerChar))
                        )
                    {
                        if (playerChar == 'X')
                        {
                            Console.WriteLine("Player 2 has won");
                        }
                        else
                        {
                            Console.WriteLine("Player 1 has won");

                        }
                        Console.WriteLine("Please press any key to reset");
                        Console.ReadKey();
                        ResetField();
                        break;
                    }
                    else if(turns==10)
                    {
                        Console.WriteLine("Draw!!");
                        Console.WriteLine("Please press any key to reset the game!");
                        Console.ReadKey();
                        ResetField() ;
                        break;
                    }
                }
                

                do
                {
                    Console.Write("Player {0}:Choose your field!", player);
                    try
                    {
                        input = int.Parse(Console.ReadLine());

                    }
                    catch (Exception)
                    {
                        Console.WriteLine("Please enter a number!");
                    }

                    if ((input == 1) && (playField[0, 0] == '1'))
                        inputCorrect = true;
                    else if ((input == 2) && (playField[0, 1] == '2'))
                        inputCorrect = true;
                    else if ((input == 3) && (playField[0, 2] == '3'))
                        inputCorrect = true;
                    else if ((input == 4) && (playField[1, 0] == '4'))
                        inputCorrect = true;
                    else if ((input == 5) && (playField[1, 1] == '5'))
                        inputCorrect = true;
                    else if ((input == 6) && (playField[1, 2] == '6'))
                        inputCorrect = true;
                    else if ((input == 7) && (playField[2, 0] == '7'))
                        inputCorrect = true;
                    else if ((input == 8) && (playField[2, 1] == '8'))
                        inputCorrect = true;
                    else if ((input == 9) && (playField[2, 2] == '9'))
                        inputCorrect = true;
                    else
                    {
                        Console.WriteLine("Incorrect Input Please use different field!");
                        inputCorrect = false;
                    }
  

                } while (!inputCorrect);


            } while (true);

        }
        public static void SetField()
        {
            Console.WriteLine("   |   |   ");
            Console.WriteLine(" {0} | {1} | {2} ", playField[0, 0], playField[0, 1], playField[0, 2]);
            Console.WriteLine("___|___|___");
            Console.WriteLine("   |   |   ");
            Console.WriteLine(" {0} | {1} | {2} ", playField[1, 0] ,playField[1, 1], playField[1, 2]);
            Console.WriteLine("___|___|___");
            Console.WriteLine("   |   |   ");
            Console.WriteLine(" {0} | {1} | {2} ", playField[2, 0], playField[2, 1], playField[2, 2]);
            Console.WriteLine("___|___|___");
            turns++;

        }
        public static void EnterXorO(int player,int input)
        {
            char playersign;
            if (player == 1)
                playersign = 'X';
            else
                playersign = 'O';

            switch (input)
            {
                case 1: playField[0, 0] = playersign; break;
                case 2: playField[0, 1] = playersign; break;
                case 3: playField[0, 2] = playersign; break;
                case 4: playField[1, 0] = playersign; break;
                case 5: playField[1, 1] = playersign; break;
                case 6: playField[1, 2] = playersign; break;
                case 7: playField[2, 0] = playersign; break;
                case 8: playField[2, 1] = playersign; break;
                case 9: playField[2, 2] = playersign; break;

            }
        }
        public static void ResetField()
        {
            char[,] playFieldInitial ={
                {'1','2','3' },
                {'4','5','6' },
                {'7','8','9' }
            };
            playField = playFieldInitial;
            SetField();
            turns = 0;

        }
    }
}
