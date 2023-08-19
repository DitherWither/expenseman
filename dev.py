#!/usr/bin/env python3
import expenseman


def main():
    app = expenseman.create_app()
    app.run(host="0.0.0.0", port=expenseman.Config.PORT, debug=True)


if __name__ == "__main__":
    main()
