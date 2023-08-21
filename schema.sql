CREATE TABLE
    IF NOT EXISTS users (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );

CREATE TABLE
    IF NOT EXISTS expenses (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        description TEXT NOT NULL,
        expense_time TIMESTAMP NOT NULL DEFAULT now(),
        user_id UUID REFERENCES users (id) ON DELETE CASCADE NOT NULL
    );

CREATE TABLE
    IF NOT EXISTS tags (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid (),
        name TEXT NOT NULL,
        user_id UUID REFERENCES users (id) ON DELETE CASCADE NOT NULL
    );

CREATE TABLE
    IF NOT EXISTS expenses_tags (
        tag UUID REFERENCES tags (id) ON DELETE CASCADE NOT NULL,
        expense_id UUID REFERENCES expenses (id) ON DELETE CASCADE NOT NULL
    );