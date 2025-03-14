# SPDX-FileCopyrightText: 2025 Nextcloud GmbH and Nextcloud contributors
# SPDX-License-Identifier: AGPL-3.0-or-later
import functools

def safe_tool(tool):
	setattr(tool, 'safe', True)
	return tool

def dangerous_tool(tool):
	setattr(tool, 'safe', False)
	return tool