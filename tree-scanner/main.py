import client.client
import server.server


def main():
    print('----- Tree Scanner -----')
    while True:
        option = input('Start the s(erver), c(lient), e(xit):')
        match option:
            case 's':
                server.main()
                break
            case 'c':
                client.main()
                break
            case 'e':
                break
            case _:
                continue


if __name__ == '__main__':
    main()
