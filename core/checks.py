"""MIT License

Copyright (c) 2020 PythonistaGuild

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from discord.ext import commands

import constants
import core


def is_role_or_higher(role_id: int):
    def predicate(ctx: core.Context):
        role = ctx.guild.get_role(role_id)

        # This should never be a problem, but just in case...
        if not role:
            # TODO: Change this to a custom exception.
            raise commands.CheckFailure(f'Role with ID <{role_id}> does not exist.')

        ignored = (constants.Roles.NITRO_BOOSTER, constants.Roles.MUTED)
        roles = [r for r in ctx.author.roles if r.id not in ignored and ctx.author.top_role >= r]

        if roles:
            return True

        # TODO: Change this to a custom exception.
        raise commands.CheckFailure(f'{ctx.author} is not in or higher than role <{role.name}(ID: {role.id})>.')
    return commands.check(predicate)
