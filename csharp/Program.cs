using System;

namespace csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.WriteLine("Using Console WriteLine, you can output any string to the terminal/console.");
            int favoriteNum = 42;
            Console.WriteLine("You can even print numbers such as the one below: ");
            Console.WriteLine(favoriteNum);
            Console.WriteLine("The {0} cow, jumped over the {1}, {2} times", "brown", "Moon", 7);
            // string name = "David";
            // Console.WriteLine(10 + " Chickens attacked " + name);
            string interpol = $"The answer to 2 + 7 is {2+7}";
            Console.WriteLine(interpol);
            Console.WriteLine("The value of pi is " + 3.14159);

            int rings = 5;
            const string name = "Kobe";
            if (rings >= 5 && name == "Kobe")
            {
                Console.WriteLine("Welcome to the party {0}, congratulations on your {1} rings.", name, rings);
            }
            else if (rings >= 5)
            {
                Console.WriteLine("You are welcome to join the party.");
            }
            else if (rings > 2)
            {
                Console.WriteLine("Decent, but {0} rings aren't enough", rings);
            }
            else
            {
                Console.WriteLine("Go win some more rings.");
            }
        }
    }
}

