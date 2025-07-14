import aiosqlite
from bot_instance import bot

async def get_db_connection():
    if not hasattr(bot, 'db_conn'):
        bot.db_conn = await aiosqlite.connect("data.db")
    return bot.db_conn

async def create_db():
    try:
        conn = await get_db_connection()
        cursor = await conn.cursor()

        await cursor.execute("""
        CREATE TABLE IF NOT EXISTS confessions (
            guild_id INTEGER PRIMARY KEY,
            num_confessions INTEGER DEFAULT 0
            )
        """)

        await conn.commit()
    except Exception as e:
        print(f"Error creating table: {e}")

async def add_confession(guild_id):
    conn = await get_db_connection()
    cursor = await conn.cursor()

    await cursor.execute(
        """
        INSERT INTO confessions (guild_id, num_confessions)
        VALUES (?, 1)
        ON CONFLICT(guild_id) DO UPDATE SET num_confessions = num_confessions + 1
        """,
        (guild_id,)
    )

    await cursor.execute("SELECT num_confessions from confessions WHERE guild_id = ?", (guild_id,))
    row = await cursor.fetchone()

    await conn.commit()
    return row[0]